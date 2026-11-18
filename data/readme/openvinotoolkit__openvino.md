Open-source software toolkit for optimizing and deploying deep learning models.

   Documentation   •   Blog   •   Key Features   •   Tutorials   •   Integrations   •   Benchmarks   •   Generative AI  

[ ](https://badge.fury.io/py/openvino)
[ ](https://www.npmjs.com/package/openvino-node)
[ ](https://anaconda.org/conda-forge/openvino)
[ ](https://formulae.brew.sh/formula/openvino)

[ ](https://pepy.tech/project/openvino)
[ ](https://anaconda.org/conda-forge/openvino/files)
[ ](https://formulae.brew.sh/formula/openvino)

- **Inference Optimization**: Boost deep learning performance in computer vision, automatic speech recognition, generative AI, natural language processing with large and small language models, and many other common tasks.
- **Flexible Model Support**: Use models trained with popular frameworks such as PyTorch, TensorFlow, ONNX, Keras, PaddlePaddle, and JAX/Flax. Directly integrate models built with transformers and diffusers from the Hugging Face Hub using Optimum Intel. Convert and deploy models without original frameworks.
- **Broad Platform Compatibility**: Reduce resource demands and efficiently deploy on a range of platforms from edge to cloud. OpenVINO™ supports inference on CPU (x86, ARM), GPU (Intel integrated & discrete GPU) and AI accelerators (Intel NPU).
- **Community and Ecosystem**: Join an active community contributing to the enhancement of deep learning performance across various domains.

Check out the [OpenVINO Cheat Sheet](https://docs.openvino.ai/2026/_static/download/OpenVINO_Quick_Start_Guide.pdf) and [Key Features](https://docs.openvino.ai/2026/about-openvino/key-features.html) for a quick reference.

## Installation

[Get your preferred distribution of OpenVINO](https://docs.openvino.ai/2026/get-started/install-openvino.html) or use this command for quick installation:

```sh
pip install -U openvino
```

### Verify Installation

After installation, you can verify OpenVINO is installed correctly by running:

```python
import openvino as ov
print(ov.__version__)
```

Check [system requirements](https://docs.openvino.ai/2026/about-openvino/release-notes-openvino/system-requirements.html) and [supported devices](https://docs.openvino.ai/2026/documentation/compatibility-and-support/supported-devices.html) for detailed information.

## Tutorials and Examples

[OpenVINO Quickstart example](https://docs.openvino.ai/2026/get-started.html) will walk you through the basics of deploying your first model.

Learn how to optimize and deploy popular models with the [OpenVINO Notebooks](https://github.com/openvinotoolkit/openvino_notebooks) 📚:
- [Create an LLM-powered Chatbot using OpenVINO](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/llm-chatbot/llm-chatbot-generate-api.ipynb)
- [YOLOv11 Optimization](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/yolov11-optimization/yolov11-object-detection.ipynb)
- [Text-to-Image Generation](https://github.com/openvinotoolkit
