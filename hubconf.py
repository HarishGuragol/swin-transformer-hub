dependencies = ['torch', "timm"]

import torch
import swin

MODEL_URLS = {
    "swin_tiny_patch4_window7_224": "https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_tiny_patch4_window7_224.pth",
    "swin_base_patch4_window7_224": "https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window7_224.pth",
    "swinv2_base_patch4_window8_256": "https://github.com/SwinTransformer/storage/releases/download/v2.0.0/swinv2_base_patch4_window8_256.pth
}

def swin_tiny_patch4_window7_224(pretrained=False):
    model = swin.SwinTransformer()
    if pretrained:
        model.load_state_dict(torch.hub.load_state_dict_from_url(MODEL_URLS["swin_tiny_patch4_window7_224"], map_location="cpu")['model'])
    return model

def swin_base_patch4_window7_224(pretrained=False):
    model = swin.SwinTransformer()
    if pretrained:
        model.load_state_dict(torch.hub.load_state_dict_from_url(MODEL_URLS["swin_base_patch4_window7_224"], map_location="cpu")['model'])
    return model
