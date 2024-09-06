import glob
import json

import mlx.core as mx
import mlx.nn as nn

from ocr.mbart import MBartConfig, MBartModel
from ocr.donut_swin import DonutSwinModel, DonutSwinModelConfig
from ocr.utils import get_model_path


class OCR(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = None
        self.decoder = None

    @staticmethod
    def from_pretrained(path_or_hf_repo: str):
        path = get_model_path(path_or_hf_repo)

        with open(path / "config.json", "r") as f:
            model_config = json.load(f)

        model = OCR()
        encoder_config = DonutSwinModelConfig.from_dict(
            model_config['encoder'])
        deconder_config = MBartConfig.from_dict(model_config['decoder'])
        donut_swin = DonutSwinModel(encoder_config)
        mbart = MBartModel(deconder_config)
        weight_files = glob.glob(str(path / "*.safetensors"))
        if not weight_files:
            raise FileNotFoundError(f"No safetensors found in {path}")

        weights = {}
        for wf in weight_files:
            weights.update(mx.load(wf))

        model.encoder = donut_swin
        model.decoder = mbart

        ds_weights = DonutSwinModel.sanitize(weights)
        mbart_weights = MBartModel.sanitize(weights)

        donut_swin.load_weights(list(ds_weights.items()))
        mbart.load_weights(list(mbart_weights.items()))

        return model
