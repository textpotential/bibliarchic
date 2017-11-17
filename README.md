# bibliarchic

This is the repository I used to write my dissertation. I did most of the writing in markdown using sublime text editor and used a simngle master branch until late in the game, when I created a revision branch to make changes more visible to my advisor. I used the GitHub integration in Slack to setup notifications on a private channel for my advisor and I, so she could see whenever I committed changes to the project and link directly to the commit. 

I used pandoc to convert the markdown into word using something like the statement below:

    pandoc --reference-docx=turabianguide07-2-10.docx -o [output_docx] -f markdown -t docx [input_md] --smart 
    
At some point, near the end of the process, I exported all of these files into word and did final revisions there to meet the requirements of our graduate studies office. All of these final revisions could have been accommodated in markdown/pandoc, with some additional time and effort, but I opted to save that work for another time. 