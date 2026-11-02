from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from models.message_model import MessageModel
from container import Container
from message_repository import MessageRepository
from message_sender import MessageSender

router = APIRouter()


@router.get('/messages/{id}', status_code=200)
@inject
def get_message(id: int, message_repository: MessageRepository = Depends(Provide[Container.message_repository_provider])):
        message =  message_repository.get_message(id)

        if message is None:
            raise HTTPException(
                status_code=404,
                detail="Message not found"
            )
        return message


@router.post('/messages', status_code=201)
@inject
def save_messages(message: MessageModel,
                        message_sender: MessageSender = Depends(
                            Provide[Container.message_sender_provider]),
                        message_repository: MessageRepository = Depends(
                            Provide[Container.message_repository_provider])):

        message_id = message_repository.save_message(message.message)

        message_sender.send_message(message.message)

        return {"id": message_id}
