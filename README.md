# News Appu
An application that consumes a news API and displays various news sources which can be viewed individually.

## Author
ESTHER WACHUKA

## Tech Used
 * python3.6
 * Flask
 * Bootstrap
 * html and css

## BDD
| Behaivour           |           |   Output        |
|--------------------|------------|-----------------|
| Display list of news sources | on page load|Display various sources of news|
| Display news per source| click on see news source|View news headlines and news previews provided by news source|
| View entire artical|click on news article| view full article in the source website|



### SETUP/INSTALLATION

#### REQUIREMENTS

* Python3.6
* pyperclip
* pip
* virtualenv
* A text  Editor
#### 1. Clone
  * In your terminal run:
    * $git clone https://github.com/washucode/newsapp
    * $cd newsapp
#### 2. Run newsapp   
   
  * Create a virtual environment and access the folder via your virtual amchine.
  * Visit https://newsapi.org/ and register for an API key.
  * Create start.sh file and in it write the following lines:
        export NEWS_API_KEY='<Your-Api-Key>'

        python3.6 manage.py server


### License
THis is licensed with MIT

### ACKNOWLEDGMENTS
 Moringa School.
 
 
### CONTACT

Talk to me : estherw8525@gmail.com
