"""
Given a list of accounts of size n where each element accounts [ i ] is a list of strings, where the first element account [ i ][ 0 ]  is a name, and the rest of the elements are emails representing emails of the account.
Geek wants you to merge these accounts. 
Two accounts definitely belong to the same person if there is some common email to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.
"""

class DisjointSet:

    def __init__(self, N:int) -> None:
        self.N = N
        self.parent = [i for i in range(N+1)]
        self.size = [1]*(N+1)

    def findParent(self, node:int) -> int:
        parent = self.parent
        if node==parent[node]:
            return node
        parent[node] = self.findParent(parent[node])
        return parent[node]
    
    def unionBySize(self, u:int, v:int):
        parent,size = self.parent, self.size
        parU = self.findParent(u)
        parV = self.findParent(v)

        if parU==parV:
            return
        
        if size[parU]<size[parV]:
            parent[parU]=parV
            size[parV] += size[parU]
        else:
            parent[parV] = parU
            size[parU] += size[parV]


from typing import List
class Solution:
    def accountsMerge(self, accounts:List[List[str]]):
        ds = DisjointSet(len(accounts))
        account_name_mapping = {}
        for i in range(len(accounts)):
            account = accounts[i][1:]
            for j in range(len(account)):
                email = account[j]
                if email in account_name_mapping:
                    # print("running union ", account_name_mapping[email], i)
                    ds.unionBySize(account_name_mapping[email],i)
                else:
                    account_name_mapping[email] = i
        # print(account_name_mapping)
        reverse_account_num = {}
        for i in range(len(accounts)):
            reverse_account_num[i] = []
        for email in account_name_mapping:
            account_number = account_name_mapping[email]
            reverse_account_num[ds.findParent(account_number)].append(email)
        # print(reverse_account_num)
        
        # print("parent debug ",ds.findParent(1))
        mergedAccounts = []
        for i in range(len(accounts)):
            if not reverse_account_num[i]:
                continue

            mergedAccounts.append([accounts[i][0]]+sorted(reverse_account_num[i]))
        return mergedAccounts

        

        

        

