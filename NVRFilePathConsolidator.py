class NVRFilePathConsolidator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimiter": ("STRING", {"default": "/"}),
                "Input1": ("STRING", {"default": "Input1"}),
            },
            "optional": {
                "Input2": ("STRING", {"default": "Input2"}),
                "Input3": ("STRING", {"default": "Input3"}),
                "Input4": ("STRING", {"default": "Input4"}),
                "Input5": ("STRING", {"default": ""}),
                "Input6": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "utils/text"

    def concatenate_text(self, delimiter, Input1, Input2="", Input3="", Input4="", Input5="", 
                         Input6=""):
        # Collect all non-empty text inputs
        text_parts = [text for text in [Input1, Input2, Input3, Input4, Input5, Input6] if text]
        
        # Join the parts with the delimiter
        result = delimiter.join(text_parts)
        
        # Remove any trailing delimiter
        if result.endswith(delimiter):
            result = result[:-len(delimiter)]
        
        return (result,)

# Add this to your NODE_CLASS_MAPPINGS
NODE_CLASS_MAPPINGS = {
    "NVRFilePathConsolidator": NVRFilePathConsolidator
}

# Add this to your NODE_DISPLAY_NAME_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = {
    "NVRFilePathConsolidator": "NVR File Path Consolidator"
}
