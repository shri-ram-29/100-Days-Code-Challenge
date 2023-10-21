class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_list = []
        invalid = [False] * len(transactions)
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            transaction_list.append({"name": name, "time": time, "amount": amount, "city": city})
        
        for i, trans1 in enumerate(transaction_list):
            if trans1["amount"] > 1000:
                invalid[i] = True
            for j, trans2 in enumerate(transaction_list):
                if i != j and trans1["name"] == trans2["name"] and trans1["city"] != trans2["city"] and abs(trans1["time"] - trans2["time"]) <= 60:
                    invalid[i] = True
        
        result = []
        for i, is_invalid in enumerate(invalid):
            if is_invalid:
                result.append(transactions[i])
        
        return result
