from fastapi import APIRouter

from app.api.v1.endpoints import (
    status,
    authen,
    users,
    category,
    post,
    product,
    product_category,
    event,
    event_category,
    project_category, project, service)

api_router = APIRouter()
api_router.include_router(status.router, tags=["StarterAPI"])
api_router.include_router(authen.router, tags=["Authen"])
api_router.include_router(users.router, prefix="/user", tags=["Users"])

api_router.include_router(post.router, prefix="/post", tags=["Post"])

api_router.include_router(category.router, prefix="/category", tags=["Category"])

api_router.include_router(product.router, prefix="/product", tags=["Product"])

api_router.include_router(product_category.router, prefix="/product_cat", tags=["ProductCat"])


api_router.include_router(event.router, prefix="/event", tags=["Event"])

api_router.include_router(event_category.router, prefix="/event_cat", tags=["EventCategory"])


api_router.include_router(project.router, prefix="/project", tags=["Project"])

api_router.include_router(project_category.router, prefix="/project_cat", tags=["ProjectCategory"])


api_router.include_router(service.router, prefix="/service", tags=["Service"])
