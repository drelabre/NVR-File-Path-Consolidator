from .NVRFilePathConsolidator import NVRFilePathConsolidator

NODE_CLASS_MAPPINGS = {
    "NVRFilePathConsolidator": NVRFilePathConsolidator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NVRFilePathConsolidator": "N-V-R File Path Consolidator"
}

print("NVR File Path Consolidator node has been locked and loaded!")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']