from app.repositories.user_profile_repository import UserProfileRepository
from app.repositories.fitness_profile_repository import FitnessProfileRepository


class UserService:
    def __init__(self, userProfileRepo: UserProfileRepository, fitnessProfileRepo: FitnessProfileRepository):
        self.userProfileRepo = userProfileRepo
        self.fitnessProfileRepo = fitnessProfileRepo

    