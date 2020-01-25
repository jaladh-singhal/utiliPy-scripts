# PDF Trimmer
Ever encountered PDFs that have redundant content on pages, most likely because they were generated from each step of PPTs with animation?

Suppose if there was two points listed on a slide with second point appearing later with animation, so there must be two pages in your PDF for that, one with only the initial point of the slide and one with the animated second point added. Now imagine that for almost every slide of presentation with as many as five points! **Lots of pages in your PDF with redundant content, right?**

Don't worry! you need not to identify & remove each of those pages from your PDF manually, when you can use this script to do all the hard work for you!

## Usage
Run script from terminal and also give location of PDF you want to trim as a command-line argument, e.g.: 
```bash
$ python pdf_trimmer.py ~/Downloads/so_bulky.pdf
```
And boom! all those annoying redundant pages will be deleted from your PDF.

The above command will do the changes in same file. If you rather want to save the changes in a new file, give another command-line argument, e.g.:
```bash
$ python pdf_trimmer.py ~/Downloads/so_bulky.pdf light_as_feather.pdf
```

## Dependencies
Make sure you have installed `PyPDF2` in your python environment. If not, simply do:
```
pip install PyPDF2
```

## Why I needed to create something like this/ Why you may need it?
I was taking a Statistics course on Coursera and they have this option to download the slides being used in videos as PDFs. Hence these PDFs had this problem because of the animations in slides as I explained above. But not any longer!

You can check yourself how this works, by comparing following two PDFs:
- [PDF containing pages with redundant content](https://drive.google.com/open?id=1ejE1e-hGocLGbaLDl5n3hm7mvtCQJvXF)
- [PDF after trimming](https://drive.google.com/open?id=1Ka2b5lFhw1U8b_w6oR4xNfj5ZUYZKc7z) by using this script

## Scope of improvement: What can you contribute?
- Extraction of plain text from PDFs is not that straightforward. Although this script worked with PDFs that I used to test it script (like one I shared in previous section), but there is a slight possiblity that it may not work with PDFs you try. For this I've added a pointer in code also.

- This script works great with eliminating redundant text, but in the process it may also lose images, like if the animation in a slide replaces previous image when new text appears.  

So if you figure out any better way to improve these, contributions are heartily welcome! 😇