from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = sa.orm.declarative_base(metadata=metadata)


class Game(Base):
    def __repr__(self):
        return (
            f"Game(id={self.id}, "
            + f"title={self.title}, "
            + f"platform={self.platform})"
        )

    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship("Review", backref=backref("game"))


class Review(Base):
    def __repr__(self):
        return (
            f"Review(id={self.id}, "
            + f"score={self.score}, "
            + f"game_id={self.game_id})"
        )

    __tablename__ = "reviews"

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey("games.id"))