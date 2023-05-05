from typing import List
from sqlalchemy.orm import Session

from server.schemas.pokemon_schema import PokemonResponse, PokemonRequest
from server.sqlalchemy.models.pokemon_model import PokemonModel


class PokemonRepository:

    @staticmethod
    def create(pokemon_request: PokemonRequest, db: Session) -> PokemonResponse:
        pokemon: PokemonResponse = PokemonModel(**pokemon_request.dict())

        db.add(pokemon)
        db.commit()
        db.refresh(pokemon)

        return pokemon

    @staticmethod
    def find_all(db: Session) -> List[PokemonResponse]:
        pokemon_list = db.query(PokemonModel).all()

        return pokemon_list

    @staticmethod
    def find_by_id(id: int, db: Session) -> PokemonResponse:
        pokemon_resp: PokemonResponse = db.query(PokemonModel).filter(PokemonModel.id == id).first()

        return pokemon_resp

    @staticmethod
    def uptade(id: int, pokemon_request: PokemonRequest, db: Session) -> PokemonResponse:
        pokemon: PokemonResponse = PokemonModel(id=id, **pokemon_request.dict())

        db.merge(pokemon)
        db.commit()

        return pokemon

    @staticmethod
    def delete_by_id(id: int, db: Session) -> PokemonResponse:
        pokemon: PokemonResponse = db.query(PokemonModel).filter(PokemonModel.id == id).first()

        if pokemon is not None:
            db.delete(pokemon)
            db.commit()

        return pokemon
