import fastapi

from app.api.routes.auth import router as auth_router
from app.api.routes.doctors import router as doctors_router
from app.api.routes.patients import router as patients_router
from app.api.routes.reservations import router as reservations_router
from app.api.routes.branches import router as branches_router

router = fastapi.APIRouter()

router.include_router(auth_router)
router.include_router(doctors_router)
router.include_router(patients_router)
router.include_router(reservations_router)
router.include_router(branches_router)
