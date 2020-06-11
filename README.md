# Tombala Game
   A Tombala Game designed with Python and Qt Designer. In this project used Python's object oriented programming and Qt Designer's GUI features. A tombala game was developed in the project, where players can play using their own names. Players can choose any card from red, green, yellow, blue, purple, lila, claret red and pink. Since there are 8 different card colors in total, a card number in the range of 1-8 is assigned to each card. The players then generate the numbers to be displayed on the cards with the help of a button and place them on the cards with format three rows fife columns. When the cards and their numbers are ready for the game, a number is drawn from the range of 1-90 with a button. The drawn stamp can be found on one of the players or both of them simultaneously. When players determine that a number on the cards is the same as the stamp, they position the stamp in the right place on the cards with the buttons in the upper right corner of their cards. The player who completes the first line on his/her card is ten points, completes the second line gets an extra twenty points, completes the third line gets an extra 40 points. The player who reaches 70 points in total and completes three lines wins the game. When the game is over, you can return to the menu and start the game again or the game will be closed.
 
 First of all, an interface with an .ui extension is designed for the game to be written with Qt Designer. The designed interface has a menu and a game screen. These two screens are on the same Main Window as the design and one is hidden while the other is visible.

<p align="center">
  <b>Menu:
  <br><br>
  <img src="https://user-images.githubusercontent.com/59059790/84407488-986f2b80-ac13-11ea-8566-4147b29fb44d.png">
</p>
 

 <p align="center">
  <b>Game:
  <br><br>
  <width=120%>
  <height=120%>
  <img src="https://user-images.githubusercontent.com/59059790/84412054-57791600-ac17-11ea-89d8-a84ae0560532.png">
</p>

The designed announcement screen should be saved in a folder. Then the location where the interface designed from the command prompt should be opened. This is done with the following code.
