from typing import Callable

from fastapi import FastAPI


def preload_model():
    """
    为了将模型加载到每个worker的内存中
    """
    from services.predict import MachineLearningModelHandlerScore

    MachineLearningModelHandlerScore.get_model()


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        preload_model()

    return start_app
