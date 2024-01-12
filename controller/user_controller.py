import logging
from fastapi import APIRouter, Request, Depends

from lib.logging_helper import LoggingHelper
from lib.mysql_helper import MysqlHelper

from model import BaseRes, BaseError, ErrorCode
from model.user import UserAddReq, UserDelReq, UserUpdateReq, UserListReq

from sql import user_dao

from service import gpt_service
from service.gpt_service import ChatAssistant

logger = logging.getLogger()
router = APIRouter(prefix=f'/user', tags=['用户相关接口'])


@router.post("/request", response_model=BaseRes)
@LoggingHelper.log_request
async def add(request: Request, payload: UserAddReq, session=Depends(MysqlHelper.depends_async_session)):
    try:
        request1 = ChatAssistant().add_messages(payload.system,payload.user)

        await user_dao.add_one(session, {
            "system": payload.system,
            "user":payload.user,
            "reply": request1
        })
    except Exception as e:
        logger.error(str(e))
        raise BaseError(*ErrorCode.UserAddError.value, scene="add")

    return {
        "code": ErrorCode.Ok.value[0],
        "msg": ErrorCode.Ok.value[1],
        "data": request1
    }
