from sample_apis.models.quiz import Quiztable
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def list_questions_api():
    try:
        # Retrieve data from the Quiztable
        questions = Quiztable.select()
        # Convert the data to a list of dictionaries
        question_list = ({
                        "question_id": question.question_id,
                        "question_text": question.question_text,
                          "correct_answer": question.correct_answer,
                          "category": question.category,
                          "difficulty_level": question.difficulty_level,
                          "explanation_text": question.explanation_text,
                          "tags": question.tags,
                          "options":question.options,
                          "total_questions":len(questions),
                          "is_active": question.is_active}
                         for question in questions)

        # Return the data as a JSON response
        return question_list
    except Exception as e:
        # Handle any exceptions that may occur during the query
        error_message = str(e)
        return HTTPException(status_code=500, detail=error_message)
