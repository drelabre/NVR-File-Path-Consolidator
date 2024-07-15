class NVRFilePathConsolidator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimiter": ("STRING", {"default": "/"}),
                "ProjectName": ("STRING", {"default": "ProjectName"}),
            },
            "optional": {
                "Date": ("STRING", {"default": "Date"}),
                "RenderType": ("STRING", {"default": "RenderType"}),
                "FileName": ("STRING", {"default": "FileName"}),
                "text5": ("STRING", {"default": ""}),
                "text6": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "utils/text"

    def concatenate_text(self, delimiter, ProjectName, Date="", RenderType="", FileName="", text5="", 
                         text6=""):
        # Collect all non-empty text inputs
        text_parts = [text for text in [ProjectName, Date, RenderType, FileName, text5, text6] if text]
        
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
