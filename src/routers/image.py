from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
import logging
from io import BytesIO
from ..COE import COE
import os

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Responses:
    @staticmethod
    def png_image_response(description: str = "A PNG image file."):
        return {
            200: {
                "description": description,
                "content": {"image/png": {}},
            },
            400: {
                "description": "Invalid input or processing error.",
            },
        }


router = APIRouter(prefix="/image", tags=["Image"])

@router.post("", description="Extract the image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the COE PDF."))
async def extract_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract coe image
        coe_image = coe_instance.get_coe_image()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        coe_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/course", description="Extract the course name image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the course name section."), )
async def extract_course_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting course name image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract course image
        course_image = coe_instance.extract_course()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        course_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/year_level", description="Extract the year level image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the academic year section."), )
async def extract_year_level_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting year level image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract year level image
        year_level_image = coe_instance.extract_acad_year()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        year_level_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/student_name", description="Extract the student name image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the student name section."))
async def extract_student_name_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting student name image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract student name image
        student_name_image = coe_instance.extract_student_name()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        student_name_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/student_no", description="Extract the student number image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the student number section."))
async def extract_student_no_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting student number image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract student no image
        student_no = coe_instance.extract_student_no()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        student_no.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/block_no", description="Extract the block number image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the block number section."))
async def extract_block_no_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting block number image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract block no image
        block_no_image = coe_instance.extract_block_no()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        block_no_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/bottom", description="Extract the bottom image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the bottom section of the COE PDF."))
async def extract_bottom_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting bottom image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract bottom image
        bottom_image = coe_instance.get_bottom_image()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        bottom_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")


@router.post("/top", description="Extract the top image of the COE PDF",
             responses=Responses.png_image_response("A PNG image of the top section of the COE PDF."))
async def extract_top_image_from_pdf(coe: UploadFile = File(...)):
    logger.info("Extracting top image from COE PDF")

    try:
        # # Ensure the uploaded file has a valid filename
        if not coe.filename or not str(coe.filename).lower().endswith('.pdf'):
            return {"error": "Invalid file type. Please upload a valid PDF file."}

        # Read the uploaded file into memory
        file_bytes = await coe.read()

        # Initialize COE object with in-memory bytes
        coe_instance = COE(file_bytes)

        # Load the COE PDF
        coe_instance.load_file()

        # Resize the image
        coe_instance.resize_image()

        # Extract top image
        top_image = coe_instance.get_top_image()

        # Convert the image to a byte stream
        img_byte_arr = BytesIO()
        top_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except AttributeError as ae:
        logger.error(f"Attribute error while processing {getattr(coe, 'filename', 'unknown file')}: {str(ae)}")
        raise HTTPException(status_code=400, detail="File processing failed. Ensure the uploaded file is a valid PDF.")
    except Exception as e:
        logger.error(f"Unexpected error while processing {getattr(coe, 'filename', 'unknown file')}: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again.")