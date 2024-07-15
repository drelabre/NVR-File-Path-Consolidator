#Welcome to the NVR File Path Consolidator.
###This node is for simplifying the task of file path naming when saving in workflows with multiple images.


####HOW TO USE:

1. Load the "NVR File Path Consolidator"
2. Place it near a Save Image node.
3. In Save Image node, convert the File Prefix widget in input.
4. In the NVR File Path Consolidator, design your file path using the widgets.
3. Convert any of the widgets you want frquently change to an input, and leave the rest as is.
4. Load a primitive node near a conveneient location (eg, near ksampler) and pipe it into the input of the NVR File Path Consolidator.
5. Create a new NVR File Path Consolidator for each Save Image node, adjust the text widget, and pipe the previously primitive to the input.


The idea is that you can plan a file path like the following examples for multiple Save Image nodes.

- ProjectName/Date/**TypeOfRender**/FileName_
- ProjectName/Date/**OriginalRender**/FileName_
- ProjectName/Date/**UpscaleRender**/FileName_
- ProjectName/Date/**FaceDetailRender**/FileName_

Note that "TypeOfRender" above could be associated for the various Saves in your workflow.

By converting the "ProjectName" on all of the NVR File Path Consolidator node to inputs and piping in from the same primitive primitive, changing the ProjectName in one primitive will change it in all the nodes.

This is a functionality that I need for some of my workflows and am sharing it in the event it's useful to anyone else.

**Full disclosure:** I am not a programmer and used Perplexity and Claude Sonnet to help me understand and develop this node.

Free to use, modidy, whatefer. Use at your own risk.
***End of transmission from The Department of Never Been Done Before.***

