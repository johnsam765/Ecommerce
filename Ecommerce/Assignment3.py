import pymongo
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        content = dict()
        connectionURI = pymongo.MongoClient(
            "mongodb+srv://mani:project123@cluster0.8cb10.mongodb.net/EcommerceDB?retryWrites=true&w=majority")
        myDB = connectionURI["EcommerceDB"]
        productsCol = myDB["Cloud9_products"]
        usersCol = myDB["Cloud9_users"]
        ordersCol = myDB["Cloud9_orders"]
        passsecureCol = myDB["Cloud9_passsecure"]
        passSecureColData = passsecureCol.find()
        allUsersData = usersCol.find()
        allOrdersData = ordersCol.find()
        usersList = []
        ordersList = dict()
        for i in passSecureColData:
            usersList.append(i["email"])
        print(usersList)
        for i in allOrdersData:
            if i["userId"] in usersList:
                ordersList[i["userId"]] = ordersCol.find(
                    {"userId": i["userId"]})
        print(ordersList)
        x = np.array(usersList)
        y = np.array([0, 0, 0, 5, 5])
        plt.figure(figsize=(20, 3))
        plt.title("No.of people purchased the products from the platform")
        plt.xlabel("Registered Users")
        plt.ylabel("People Purchased")
        plt.bar(x, y, color='black', width=.1)
        plt.legend()
        plt.show()
    except Exception as e:
        print("Error in the connection string")
        print(e)


main()

# def createDB():  # Database creation
#     try:
#         myDB = connectionURI["e-Commerce"]
#         print(f"--  database has been created successfully --")
#         return myDB

#     except Exception as e:
#         print("xx Error connecting to the database "+" xx")
#         print(e)
#         print("-----")


# def createCollection(database, collectionName):  # Creating Collections
#     try:
#         users = database[collectionName]
#         print(f"-- {collectionName} collection has been created successfully --")
#         return users
#     except Exception as e:
#         print("xx Error creating the collection "+collectionName+" xx")
#         print(e)
#         print("-----")


# def insertData(coll, data):  # Data insertion
#     try:
#         coll.insert_one(data)
#         print(f"Data inserted succesfully in the {coll} table")
#     except Exception as e:
#         print("xx Error occured while inserting data "+data+" xx")
#         print(e)
#         print("-----")


# def displayData(coll):  # Data Display
#     allData = coll.find()
#     try:
#         for i in allData:
#             print(i)
#         print("-- End of data --")
#     except Exception as e:
#         print("xx Error occured while displaying data xx")
#         print(e)
#         print("-----")


# def updateData(coll, param, query):
#     try:
#         coll.update_one(param, query)
#         print("Updated Successfully")
#     except Exception as e:
#         print("xx Error occured while updating data xx")
#         print(e)
#         print("-----")


# def main():
#     try:
#         # database = createDB()
#         # users = createCollection(database, "Users")
#         # # 5 documents for the collection Users
#         # insertData(users, {"first_name": "John Samuel", "last_name": "Lawrence",
#         #            "email": "johnsamuel.765@gmail.com", "Account No.": "xxxx678", "age": 24})
#         # insertData(users, {"first_name": "Kailash", "last_name": "Kanchipuram Sivakumar",
#         #            "email": "kailash.sivakumar@gmail.com", "Account No.": "xxxx564", "age": 25})
#         # insertData(users, {"first_name": "Sheethal", "last_name": "Joy",
#         #            "email": "sheethal.joy@gmail.com", "Account No.": "xxxx746", "age": 14})
#         # insertData(users, {"first_name": "Isaac", "last_name": "Philip",
#         #            "email": "isaac.philip@gmail.com", "Account No.": "xxxx132", "age": 10})
#         # insertData(users, {"first_name": "Jeffrey", "last_name": "Godson",
#         #            "email": "jeff.123@gmail.com", "Account No.": "xxxx946", "age": 34})
#         # bankRecords = createCollection(database, "BankRecords")
#         # # 5 documents for the collection Bank Records
#         # insertData(bankRecords, {"Account No.": "6785678", "Credit Balance": 2500,
#         #            "Account Balance": 10000, "Account type": "Student", "No. of account": 2})
#         # insertData(bankRecords, {"Account No.": "6775645", "Credit Balance": 500,
#         #                          "Account Balance": 4500, "Account type": "Fixed Deposit", "No. of account": 1})
#         # insertData(bankRecords, {"Account No.": "6705634", "Credit Balance": 1500,
#         #                          "Account Balance": 4564, "Account type": "Chequing", "No. of account": 3})
#         # insertData(bankRecords, {"Account No.": "7865645", "Credit Balance": 700,
#         #                          "Account Balance": 9685, "Account type": "Savings", "No. of account": 1})
#         # insertData(bankRecords, {"Account No.": "9078645", "Credit Balance": 100,
#         #                          "Account Balance": 9362, "Account type": "Student", "No. of account": 4})
#         # # 5 Query updates
#         # updateData(users, {"first_name": "John Samuel"},
#         #            {"$set": {"first_name": "John"}})
#         # bankRecords.update_many({"Account type": "Student"}, {
#         #     "$set": {"Student Discount": True}})
#         # updateData(bankRecords, {"Account No.": "6785678"},
#         #            {"$set": {"Credit Balance": 500}})
#         # updateData(bankRecords, {"Account No.": "7865645"},
#         #            {"$set": {"Notes": "Address proof check"}})
#         # updateData(bankRecords, {"first_name": "Isaac"},
#         #            {"$set": {"first_name": "Isaac J"}})
#         # # Query set condition
#         # studentsData = bankRecords.find({"Account Type": "Student"})
#         # for i in studentsData:
#         #     print(i)
#         # print("-----")
#         # account6Series = bankRecords.find({"Account No.": {"$regex": "6*"}})
#         # for j in account6Series:
#         #     print(j)
#         # print("-----")
#         # balanceGt1k = users.find(
#         #     {"$and": [{"age": {"$gt": 15}}, {"first_name": "Sheethal"}]})
#         # for k in balanceGt1k:
#         #     print(k)
#         #     print("-----")
#         # balanceGt2k = bankRecords.find(
#         #     {"$or": [{"No. of accounts": {"$gt": 2}}, {"Credit Balance": {"$gt": 1000}}]})
#         # for l in balanceGt2k:
#         #     print(l)
#         #     print("-----")
#         # balanceGt3k = bankRecords.find(
#         #     {"$or": [{"Account Type": "Student"}, {"No. of account": {"$lt": 2}}]})
#         # for m in balanceGt2k:
#         #     print(m)
#         #     print("-----")
#         # # Deletion Events
#         # users.delete_one({"first_name": "John"})
#         # bankRecords.delete_many({"Account type": "Student"})
#         # users.delete_many({"age": {"$gt": 20}})
#         # bankRecords.delete_many({"Credit Balance": {"$gt": 2000}})
#         # bankRecords.delete_many({"No. of account": 2})
#         # # Documents display
#         # displayData(users)
#         # displayData(bankRecords)

#     except Exception as e:
#         print("Error in the connection string")
#         print(e)


# main()
