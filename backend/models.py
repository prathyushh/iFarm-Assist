from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .database import Base

class UserRole(str, enum.Enum):
    FARMER = "FARMER"
    EXPERT = "EXPERT"
    ADMIN = "ADMIN"

class QueryStatus(str, enum.Enum):
    PENDING = "PENDING"
    SOLVED = "SOLVED"
    ESCALATED = "ESCALATED"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.FARMER)
    location = Column(String, nullable=True)
    crops_grown = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    queries = relationship("Query", back_populates="owner")
    escalations_handled = relationship("Escalation", back_populates="expert")

class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    input_type = Column(String) # TEXT, VOICE, IMAGE
    heading = Column(String, nullable=True) # Short summary for list view
    original_input = Column(Text) # Transcribed text or text input
    media_url = Column(String, nullable=True) # URL for Image/Audio
    enriched_prompt = Column(Text, nullable=True)
    
    ai_response_text = Column(Text, nullable=True)
    confidence_score = Column(Float, default=0.0)
    
    status = Column(Enum(QueryStatus), default=QueryStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="queries")
    escalation = relationship("Escalation", back_populates="query", uselist=False)
    feedback = relationship("Feedback", back_populates="query", uselist=False)

class Escalation(Base):
    __tablename__ = "escalations"

    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("queries.id"))
    expert_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    expert_response = Column(Text, nullable=True)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    expert_notes = Column(Text, nullable=True)

    query = relationship("Query", back_populates="escalation")
    expert = relationship("User", back_populates="escalations_handled")

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("queries.id"))
    is_helpful = Column(Boolean)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    query = relationship("Query", back_populates="feedback")
