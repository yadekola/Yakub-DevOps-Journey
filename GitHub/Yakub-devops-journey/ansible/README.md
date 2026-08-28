# Ansible

## The idempotency test

```bash
ansible-playbook -i inventories/hosts.ini site.yml
ansible-playbook -i inventories/hosts.ini site.yml   # run it again
```

Second run must show `changed=0`. If it does not, find the task that keeps reporting
changed. It is almost always a `shell` or `command` task — those cannot know whether
anything changed, so they always report changed.

## Secrets

Never put passwords in `group_vars` in plaintext. Use:

```bash
ansible-vault encrypt group_vars/all/vault.yml
ansible-playbook site.yml --ask-vault-pass
```

Encrypted vault files are safe to commit. Unencrypted ones are not.
