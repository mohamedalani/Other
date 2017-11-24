# Analysing the Enron emails dataset**
A Challenge I have done for the recruitment process of Digital Genius.
## Part 1 : 
The dataset consists of message strings sitting in a single column, and containing
information about senders, recipients, timestamps, subjects and the content of the
messages themselves. You should write a procedure to parse this dataset into message
instances. 
## Part 2 : 
**Option​ ​2**:​ ​Making​ ​messages​ ​available​ ​via​ ​a​ ​RestAPI
Write a simple application that will return an array of messages depending on some request
parameters. Structure your API to be able to filter messages according to the following:
- Sender address
- Recipient addresses (may be one or more)
- Sending time range


----
To run the scripts : 
1. Download the dataset here : https://www.kaggle.com/wcukierski/enron-email-dataset/data
2. Change the path in part1.py and part2.py to read emails.csv 
3. run part1.py to extract the mails and store them in a sqlite database
4. run part2.py to launch the server "http://127.0.0.1:5002/" and begin to write some requests you like.

  Returns filtered json emails from Enron database.

* **URL**

  /sender/:sender_mail
  
  /recipient/:recipient_mails

  /date_range/:dates
* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `sender_mail=[string]`
   `recipient_mails=[string,...,string]`
   `dates=[date1,date2]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "mails found": [
    {
      "content": " Hello, :) Best regards, Sally  ",
      "date": "2000-01-01",
      "receiver": "fernley.dyson@enron.com",
      "sender": "sally.beck@enron.com",
      "subject": ": Happy New Year - No Y2K Fear!",
      "time": "14:36:00"
    }]}`
 
* **Error Response:**
  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "No mails found" }`


* **Sample Call:**

  `http://127.0.0.1:5002/date_range/2000-01-01,2000-01-02`