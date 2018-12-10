select * from learn_student;
select * from auth_user;

-- delete from auth_user where id=4;
delete from learn_task; -- where idTask=7;

insert into learn_task values (1, 1, 'Enter the following code into the new shell window:;; print("Hello World!");;
and run it.;The "print" command displays everything inside the parentheses to the console.');

insert into learn_task values (2, 1, 'Normally, when asked to find the product of two numbers like
8 × 3.57, you would use a calculator or a pencil and paper. Well,
how about using the Python to perform your calculation?
Let’s try it. Calculate 1.11 x 70 and print it.; The basic symbols used by Python to perform
mathematical operations are called "operators":;; + Addition; - Subtraction; * Multiplication; / Division;;
We can also change the order of operations by adding parentheses like:;;(2+2)*2');

insert into learn_task values (3, 1, 'Create a new variable "luck" with 777 value and print it.; The word "variable" 
in programming describes a place to store information
such as numbers, text, lists of numbers and text, and so on. Another way of looking at a variable 
is that it’s like a label for something.;
To create a variable named "dollar", we use an equal sign (=) and then tell Python what information the 
variable should be the label for. Here, we create the variable "dollar" and tell Python that it labels the 
number 100;; dollar = 100;;To print the variable you should write:;;print(dollar)');

insert into learn_task values (4, 1, 'We can also tell Python to change the variable "dollar" so that it
labels something else. For example, here’s how to change "dollar" to the number 200;; dollar = 200;;
We can also use more than one variable
for the same item;;dollar=200; euro=dollar;;Now command;;print(euro);; display 200;TASK:; Set luck as 13;
Print it.; Then set luck 77;Print it again;;P.S. Variable names 
can be made up of letters, numbers, and the underscore character (_), but they can’t start with a number.');

insert into learn_task values (5, 1, 'We can use variables in our calculations like;;
coins=5;bonus=coins*0.5;print(coins+bonus);; TASK:;
Let''s solve the puzzle. The girl cut out of paper 5 squares, 
7 triangles, and 2 times more circles than triangles. How many figures did the girl cut out?;
All values you should save to variable and print result.');

insert into learn_task values (6, 1, 'STRINGS:;In programming terms, we usually call text a string. When you
think of a string as a collection of letters, the term makes sense.
All the letters, numbers, and symbols could be a string. In Python, we create a string by putting
quotes around text. For example:;;name = "Anna";;You can also use single quotes to create a string, like this:;;
address = ''Ukrain, Kiev'';;To use more than one line of text in your string (called a
multiline string), use three single quotes (''''''), and then hit enter
between lines, like this:;;fred = ''''''How do dinosaurs pay their bills?;
With tyrannosaurus checks!'''''';;TASK:;Let''s repeet 1 task:; Create variable "hello_string" 
and set it "Hello World!";Print this variable.');

insert into learn_task values (7, 1, 'Now consider this crazy example of a string, which causes Python
to display an error message:;;silly_string = ''He said, "Aren''t can''t shouldn''t wouldn''t."''
;;The solution to this problem is a multiline string, which we learned about earlier, using three 
single quotes (''''''), which allows us to combine double and single quotes in our string without
causing errors.;But if you really want to use single or double quotes to 
surround a string in Python, instead of three single quotes, you can add a backslash (\) before 
each quotation mark within the string. This is called escaping. It’s a way of saying to
Python, “Yes, I know I have quotes inside my string, and I want
you to ignore them until you see the end quote.” So, now our string will be look like this:;;
 single_quote_str = ''He said, "Aren\\''t can\\''t shouldn\\''t wouldn\\''t."'';TASK:;Create variable "history"
 and set value;;She asks, "Can I take your pen, isn''t it?".;; and print it.');
 
 insert into learn_task values (8, 1, 'EMBEDDING VALUES IN STRINGS:;If you want to display a 
 message using the contents of a variable, you can embed values in a string using %s, which is like a
marker for a value that you want to add later. For example, to have store the 
number of points you scored in a game, and then add it to a sentence like “I scored __ points,” use
%s in the sentence in place of the value, and then tell Python that value, like this:;;
myscore = 1000;message = ''I scored %s points'';print(message % myscore);; You get "I scored 1000 points";
You can also use more than one placeholder in a string, like this:;;nums = ''What did the number %s say to 
the number %s? Nice belt!!'';print(nums % (0, 8));;You get "What did the number 0 say to the number 8? Nice belt!!";
TASK: Create a variable "template" with value "%s wants to have a grade %s.". Then define a variables name and grade. 
Set them the values ​​"Nastya" and "A" respectively. Substitute these values into a template and print the result.');

insert into learn_task values (9, 1, 'MULTIPLYING STRINGS:; What is 10 multiplied by 5? The answer is 50, of course. 
But what’s 10 multiplied by "a"?:;;print(10 * "a");; result is "aaaaaaaaaa". You can create a big indents with 
same sizes:;;spaces = ' ' * 15;print(''%sUkrain, Kiev'' % spaces);print(''%sKhreshchatic street'' % spaces);;
This code display text on the right part of the console.; TASK:;Create string "LoL" with the same value. 
Print this variable 10 times.');

insert into learn_task values (10, 1, 'LISTS:;“Spider legs, toe of frog, eye of newt, bat wing,
slug butter, and snake dandruff” is not quite a normal shopping list (unless you happen to be
a wizard), but we’ll use it as our first example of the differences between strings and lists. 
We could store this list of items in the wizard_list variable using a string. But we could also create 
a list, a somewhat magical kind of Python object that we can manipulate. Here’s what these items
would look like written as a list:;;wizard_list = ["spider legs", "toe of frog", "eye of newt",
"bat wing", "slug butter", "snake dandruff"];;TASK:;Create a list named subjects with items "Math", "Music",
"Literature" and "Chemistry". Print it.' );

insert into learn_task values (11, 1, 'INDEXING:;Creating a list takes a bit more typing than creating a string,
but a list is more useful than a string because it can be manipulated. For example, we could print the third
 item in the wizard_list (eye of newt) by entering its position in the list (called the index
position) inside square brackets ([]), like this:;;print(wizard_list[2]);;!!! lists start at
index position 0, so the first item in a list is 0, the second is 1, and the third is 2.We can also 
change an item in a list much more easily than we could in a string. Perhaps instead of eye of newt 
we needed a snail tongue:;; wizard_list[2] = ''snail tongue'';;TASK:;Create a list named subjects with 
items "Math", "Music","Literature" and "Chemistry". Change last element to "Biology". Print the list.');

insert into learn_task values (12, 1, 'SLICES:;Another option is to show a subset
of the items in the list. We do this by using a colon (:) inside square brackets.
For example, enter the following to see the third to fifth items in a list:;; print(wizard_list[2:5]);;
Writing [2:5] is the same as saying, “show the items from index position 2 up to (but not including) 
index position 5”—or in other words, items 2, 3, and 4.; TASK:;Create a list named fruits with items 
apples, pears, plums and apricots (don''t forget to put them in quotes). Print elements 1 and 2');

insert into learn_task values (13, 1, 'LISTS:;Lists can be used to store all sorts of items, like numbers:;;
 some_numbers = [1, 2, 5, 10, 20];;They can also hold strings or might have mixtures of numbers and strings:;;
 numbers_and_strings = ["Why", 7, "because", 7, 9];;And lists might even store other lists:;;
 numbers = [1, 2, 3, 4];strings = ["I", "kicked"]; mylist = [numbers, strings];print(mylist);;Result is:
 [[1, 2, 3, 4], ["I", "kicked"]];TASK:;Create a list named quirk that keep items 1, "two" and other list with 
 items 3, "four". Print this list.');

insert into learn_task values (14, 1, 'ADDING ITEMS TO A LIST:;To add items to a list, we use the append 
function. A function is a chunk of code that tells Python to do something. In this case, append
adds an item to the end of a list. For example, to add a "Ukrain" to europ, do this:;;
europ = ["Belgium", "France", "Germany", "Italy"];europ.append("Ukrain"); print(europ);;Result is:
["Belgium", "France", "Germany", "Italy", "Ukrain"];TASK:;Create a list named planets with items 
"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus" and "Neptune". Add a new planet named "Pluto".
Print new list.');








