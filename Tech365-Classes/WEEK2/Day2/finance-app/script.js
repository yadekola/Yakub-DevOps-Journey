let transactions = JSON.parse(localStorage.getItem("transactions")) || [];
      let editId = null;
      updateUI();

      function addTransaction() {
        let desc = document.getElementById("desc").value;
        let amount = parseFloat(document.getElementById("amount").value);
        let type = document.querySelector('input[name="type"]:checked').value;

        if (!desc || isNaN(amount) || amount <= 0) return;

        if (editId) {
          const transactionIndex = transactions.findIndex(
            (t) => t.id === editId
          );
          transactions[transactionIndex] = {
            id: editId,
            desc,
            amount,
            type,
            date: new Date().toLocaleDateString(),
          };
          editId = null;
        } else {
          transactions.push({
            id: Date.now(),
            desc,
            amount,
            type,
            date: new Date().toLocaleDateString(),
          });
        }

        localStorage.setItem("transactions", JSON.stringify(transactions));
        document.getElementById("desc").value = "";
        document.getElementById("amount").value = "";
        updateUI();
      }
      function formatCurrency(value) {
        return value.toLocaleString("en-NG", {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });
      }

      function updateUI() {
        let income = transactions
          .filter((t) => t.type === "income")
          .reduce((sum, t) => sum + t.amount, 0);
        let expense = transactions
          .filter((t) => t.type === "expense")
          .reduce((sum, t) => sum + t.amount, 0);
        let balance = income - expense;

        document.getElementById("balance").innerText = formatCurrency(balance);
        document.getElementById("income").innerText = formatCurrency(income);
        document.getElementById("expense").innerText = formatCurrency(expense);

        let transactionList = document.getElementById("transactions");
        transactionList.innerHTML = transactions
          .map(
            (t) => `
                <li>
                    <div class="date">${t.date} </div> <span> ${t.desc} </span>
                    <span class="${t.type}">${
              t.type === "income" ? "" : ""
            } &#8358;${formatCurrency(t.amount)}</span>
                    <span onclick="editTransaction(${t.id})">
                        <i class="ri-edit-box-line"></i>
                    </span>
                    <span onclick="deleteTransaction(${t.id})">
                        <i class="ri-delete-bin-line delete"></i>
                    </span>
                   
                </li>
            `
          )
          .join("");
      }

      function deleteTransaction(id) {
        transactions = transactions.filter((t) => t.id !== id);
        localStorage.setItem("transactions", JSON.stringify(transactions));
        updateUI();
      }

      function editTransaction(id) {
        const transaction = transactions.find((t) => t.id === id);
        if (transaction) {
          document.getElementById("desc").value = transaction.desc;
          document.getElementById("amount").value = transaction.amount;
          document.querySelector(
            `input[name="type"][value="${transaction.type}"]`
          ).checked = true;
          editId = id;
        }
      }