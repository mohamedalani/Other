**Analysing the Enron emails dataset**
----
To run the scripts : 
1. Change the path to get your csv in part1.py and part2.py
2. run part1.py to extract the mails and store them in a sqlite database
3. run part2.py to lauch the server "http://127.0.0.1:5002/" and begin to write some requests you like.

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

  ```http://127.0.0.1:5002/date_range/2000-01-01,2000-01-02
  ```