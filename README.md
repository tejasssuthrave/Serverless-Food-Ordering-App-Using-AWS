# 🍔 Serverless Food Ordering Web Application

A **Serverless Food Ordering Web Application** built using AWS cloud services.
This project demonstrates how a frontend hosted on **Amazon S3** can interact with backend APIs using **API Gateway** and **AWS Lambda**, with **DynamoDB** used for storing menu and order data.

---

## 🚀 Architecture Overview

User (Browser)
↓
Amazon S3 (Static Website Hosting)
↓
API Gateway (REST APIs)
↓
AWS Lambda (Serverless Backend)
↓
DynamoDB (Database)

---

## 🏗️ Architecture Diagram

<img width="1024" height="1536" alt="ChatGPT Image Mar 8, 2026, 04_44_21 PM" src="https://github.com/user-attachments/assets/af1c9c25-c827-49c6-8759-f409fa0fbc76" />


---

## ⚙️ AWS Services Used

| Service     | Purpose                           |
| ----------- | --------------------------------- |
| Amazon S3   | Hosts the static frontend website |
| API Gateway | Provides REST API endpoints       |
| AWS Lambda  | Handles backend logic             |
| DynamoDB    | Stores menu items and order data  |

---

## 📋 Features

* View food menu dynamically
* Place food orders
* Store order details in DynamoDB
* Fully serverless architecture
* Scalable and cost-efficient cloud application

---

## 📂 Project Structure

```
food-ordering-app
│
├── index.html
├── style.css
├── script.js
├── architecture.png
└── README.md
```

---

## 🔄 Application Workflow

1. User opens the website hosted on **Amazon S3**
2. Frontend sends API request to **API Gateway**
3. API Gateway triggers **AWS Lambda**
4. Lambda fetches or stores data in **DynamoDB**
5. Response is sent back to the frontend

---

## 📡 API Endpoints

### Get Menu

Method: **GET**

```
/Get-menu
```

Returns list of available food items.

Example Response:

```
[
  {
    "id": 1,
    "food_name": "Pizza",
    "price": 250
  },
  {
    "id": 2,
    "food_name": "Burger",
    "price": 150
  }
]
```

---

### Place Order

Method: **PUT**

```
/place-order
```

Example Request Body:

```
{
 "user": "Tejas",
 "food": "Pizza",
 "quantity": 2
}
```

---

## 🛠️ Technologies Used

* HTML
* CSS
* JavaScript
* Amazon S3
* AWS API Gateway
* AWS Lambda
* Amazon DynamoDB

---

## 🎯 Learning Outcomes

Through this project I learned:

* Building **serverless cloud applications**
* Integrating **frontend with REST APIs**
* Using **AWS Lambda for backend logic**
* Storing data using **DynamoDB**
* Deploying static websites using **Amazon S3**

---

## 📸 Deployment

The frontend can be deployed using **Amazon S3 Static Website Hosting** and connected to API Gateway endpoints.

---

## 📂 GitHub Repository

You can find the project code here:

```
https://github.com/tejasssuthrave/Serverless-Food-Ordering-App-Using-AWS
```

---

## ⭐ Support

If you found this project useful, consider giving the repository a **star ⭐**.
