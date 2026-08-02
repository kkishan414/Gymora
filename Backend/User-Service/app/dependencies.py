from app.db.mongodb import get_database
from app.repositories.fitness_profile_repository import FitnessProfileRepository
from app.repositories.user_profile_repository import UserProfileRepository
from app.services.user_service import UserService

def get_user_profile_repository():
    db = get_database()
    return UserProfileRepository(db)

def get_fitness_profile_repository():
    db = get_database() 
    return FitnessProfileRepository(db)

def get_user_service():
    user_profile_repo = get_user_profile_repository()
    fitness_profile_repo = get_fitness_profile_repository() 
    return UserService(user_profile_repo, fitness_profile_repo)