FROM continuumio/miniconda3:latest
WORKDIR /app
COPY environment.yaml .
RUN conda env create -f environment.yaml
RUN echo "conda activate ireland-forest-carbon" >> ~/.bashrc
SHELL ["/bin/bash", "-c", "source /opt/conda/bin/activate ireland-forest-carbon && $@"]
COPY . .
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
