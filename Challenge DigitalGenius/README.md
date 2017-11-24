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

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `sender_mail=[string]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```