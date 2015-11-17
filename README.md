# client_side_authoring
An XBlock that provides an authoring interface for the client-side aspects of XBlock, for authors that only want to use the HTML/css/javascript web technologies. 

This is a basic proof of concept, which provides the following:

* a wysiwyg authoring interface for people who are mostly doing layout and formatting,
* a raw interface for people who know HTML/CSS/Javascript and who want to control the page in ways for which the wysiwyg interface doesn't provide a button
* a viewing interface for the student-facing result of all that authoring work.
* a callback for getting and setting student state on the server-side
* Improving the GUI so that the authoring interfaces are pre-seeded with the current authored state


There's still a lot of work to be done:

* Integrating the authoring GUI into studio and other aspects of edx-platform
* Improving security so that author-provided client-side code is isolated from concurrently displayed client-side code (may involve contributions to XBlock)
* Providing a client-side accessible callback into a grading system, allowing this XBlock to compete with JSInput 

This is still in active development, and will not have backwards compatibility until it is more officially released. If you are looking at this repository, I hope that you will be interested in the conceptual discussion of what this is trying to do. Feel free to start a conversation with me at lylaedx (at) gmail.com. 
