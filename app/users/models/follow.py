# """Module for representing followers in the system"""
# from datetime import datetime
#
# from sqlalchemy import Column, Integer, DateTime, ForeignKey
# from sqlalchemy.orm import relationship, backref
#
# from app.db import Base
#
#
# class Follow(Base):
#     __tablename__ = "follows"
#
#     customer_id = Column(Integer, ForeignKey("customers.id"), primary_key=True)
#     artist_id = Column(Integer, ForeignKey("artists.id"), primary_key=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     customer = relationship("Customer", backref=backref("follows_assoc"))
#     artist = relationship("Artist", backref=backref("follows_assoc"))
