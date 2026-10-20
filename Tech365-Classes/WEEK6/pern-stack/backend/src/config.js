// Containers receive these values from Compose. Local runs use --env-file.
export function configFromEnv(env = process.env) {
  for (const key of ['POSTGRES_DB', 'POSTGRES_USER', 'POSTGRES_PASSWORD']) {
    if (!env[key]) throw new Error(`Missing required environment variable: ${key}`);
  }
  const port = Number(env.PORT || 3000);
  const dbPort = Number(env.DB_PORT || 5432);
  if (![port, dbPort].every(p => Number.isInteger(p) && p > 0 && p <= 65535)) {
    throw new Error('PORT and DB_PORT must be valid TCP ports.');
  }
  return {port, database: {
    host: env.DB_HOST || 'db', port: dbPort,
    database: env.POSTGRES_DB, user: env.POSTGRES_USER,
    password: env.POSTGRES_PASSWORD,
    max: 10, connectionTimeoutMillis: 5000, idleTimeoutMillis: 30000,
    statement_timeout: 5000,
  }};
}
