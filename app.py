import os, sys
from src.pipeline.pipeline import Pipeline


def start_pipeline():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise Exception(e, sys) from e

start_pipeline()