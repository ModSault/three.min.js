# Three.min.js

A fork of [Three.js](https://github.com/mrdoob/three.js) that is just meant to take up significantly less space on a hard drive. I've made a site using vanilla JS, CSS, and HTML. Then I made a page that required ThreeJS. Since you usually use NPM for that and vanilla webpages don't have access to that, I either had to use npm for one specific webpage that also needed to grab a file from one directory back, or I could just use a submodule and grab the files that way. I could also use a CDN but they lack certain files and make my site not work offline so I didn't do that either. I opted on the latter method for the submodule as it seems simpler.
<br><br>
So why my own fork? Well the main repo takes up a lot of space. On top of the fact that cloning it takes forever, GitHub pages has a soft limit of 1gb. So I made this fork to remove all the fat from the repo and make deploying the site easier.
```
Old size:
size: 595 MB (624,048,460 bytes)
size on disk: 606 MB (635,609,088 bytes)

New Size:
size: 21.2 MB (22,232,176 bytes)
size on disk: 23.2 MB (24,350,720 bytes)
```