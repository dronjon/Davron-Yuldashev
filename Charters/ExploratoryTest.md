Exploratory testing of Monefy App on iOS (13.3.1)

Charter 1: Analyze the ‘New Income’ functionality of the Monefy app.

Actor: Normal user

Purpose: To evaluate the new record functionality where user can create a ‘new income’.

Setup: iPhone 7 with iOS 13.3.1, Monefy 1.3.3

Priority: High because this functionality is critical for users and one of the principle objectives of the application.

Start: Mon, March 2, 2020

Duration: Short(30-60mins)

Test Notes:

	Step 1. Open the app and tap on the “+” (plus) icon at the bottom right of the screen. 

    •	You are taken to ‘new income’ screen

Step 2. Tap on the ‘date’. Select any other day and tap ‘ok'.
    •	Since this is a new entry, the purpose here is not to create an entry for other day, rather, it is just to make sure that calendar is opening, and you can select another day.  
        Once you make sure of that, change the date back to ‘todays date’ and continue

Step 3. Enter an integer or a float number into the input field.

    •	The initial value of the input field is set to zero and you should be able to insert nine whole numbers and tenth character being decimal separator

Step 4. Select whether new entry is placed in ‘cash’ or ‘credit card’ account.

    •	You should be able to make a selection of where you want to position your new income entry

Step 5. Perform basic calculating operations

    •	You should be able to perform basic arithmetic calculations, as calculator functionality is integrated as part the ‘new record’  

Step 6. Enter a note.

    •	The note can be any character and doesn’t have a limit. Note is also not mandatory, you can continue without it.

Step 7. Tap ‘choose a category’.

    •	Once you are done with a note and inserting value into input field you should have the option of choosing a category. 
        Since this is a new income entry, you should be given four options as per to where you will place the ‘new income’ entry. 
        You can save it as ‘deposits’, ‘salary’, ‘savings’ and also the option of adding it to a ‘new category’. 
        You should be able to save the entry in all four ends. 

Step 8. Verify that ‘new entry’ was successful.

    •	After you select one of the options above, you are taken to the main screen where you should be able to see your ‘new entry’. 
        If there were other entries in ‘income’ category, the amount you entered as part of this test should be added to the previous amount. 
        If that is the case, you will have to verify the added amount to the previous amount, otherwise verify the initial amount. 
        There are several ways to verify this. 
        One is the ‘new entry’ amount should be visible in the center circle on the main screen. 
        The other is you tap on balance and verify the entry in list. 

Bugs: No bugs were discovered during this test.


Charter 2: Analyze the ‘New Expense’ functionality of the Monefy app. (First half of this charter is similar to Charter 1 because it involves creating a new record)

Actor: Normal user

Purpose: To evaluate the new record functionality where user can create a ‘new expense’.

Setup: iPhone 7 with iOS 13.3.1, Monefy 1.3.3

Priority: High because this functionality is critical for users and one of the principle objectives of the application.

Start: Mon, March 2, 2020

Duration: Short(30-60mins)

Test Notes:

	Step 1. Open the app and tap on the “-” (minus) icon at the bottom right of the screen. 

    •	You are taken to ‘new expense’ screen

Step 2. Tap on the ‘date’. Select any other day and tap ‘ok'.

    •	Since this is a new entry, the purpose here is not to create an entry for other day, rather, it is just to make sure that calendar is opening, 
        and you can select another day. 
        Once you make sure of that, change the date back to ‘todays date’ and continue

Step 3. Enter an integer or a float number into the input field.

    •	The initial value of the input field is set to zero and you should be able to insert nine whole numbers and tenth character being decimal separator

Step 4. Select whether new entry is placed in ‘cash’ or ‘credit card’ account.

    •	You should be able to make a selection of where you want to position your new income entry

Step 5. Perform basic calculating operations

    •	You should be able to perform basic arithmetic calculations, as calculator functionality is integrated as part the ‘new record’  

Step 6. Enter a note.

    •	The note can be any character and doesn’t have a limit. Note is also not mandatory, you can continue without it.

Step 7. Tap ‘choose a category’.

    •	Once you are done with a note and inserting value into input field you should have the option of choosing a category. 
        Since this is a new expense entry, you should be given a list of options as per to where you will place the ‘new expense’ entry. 

Step 8. Verify that ‘new entry’ was successful.

    •	After you select one of the category options, you are taken to the main screen where you should be able to see your ‘new entry’. 
        If there were other entries in ‘income’ category, the amount you entered as part of this test should be added to the previous amount. 
        If that is the case, you will have to verify the added amount to the previous amount, otherwise verify the initial amount. 
        There are several ways to verify this. One is the ‘new entry’ amount should be visible in the center circle on the main screen. 
        The other is you tap on balance and verify the entry in list. 

Step 9. Create and verify a ‘new expense’ entry from the main screen.

    •	There is also an option to create a ‘new expense’ by taping on category icons. 
        Above steps should be followed and new record should be created. 
        There are several ways to verify this. One is that, once you add a new expense, a correct number should be displayed in the middle circle, as well as by tapping on 
        ‘Balance’ and seeing it in the list of other entries. Another way is that you should be able to see a percentage of that expense 
        (depending on all the given expenses for that period) under the icon of the category you have selected. 


Bugs: No bugs were discovered during this test.


