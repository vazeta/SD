from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from app.models import Project, Employee, Counter

router = APIRouter()

# Create Jinja2 template instances for two template directories.
templates = Jinja2Templates(directory="app/templates")
servlet_templates = Jinja2Templates(directory="app/servlet_templates")

# In-memory list to store projects.
project_list = []

@router.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/greeting")

@router.get("/greeting", response_class=HTMLResponse)
async def greeting(request: Request, name: str = "World"):
    return templates.TemplateResponse("greeting.html", {
        "request": request,
        "name": name,
        "othername": "SD"
    })

@router.get("/givemeatable", response_class=HTMLResponse)
async def give_me_a_table(request: Request):
    employees = [
        Employee(id=1, name="José", telephone="9199999", salary=1890),
        Employee(id=2, name="Marisa", telephone="9488444", salary=2120),
        Employee(id=3, name="Hélio", telephone="93434444", salary=2500),
    ]
    return templates.TemplateResponse("table.html", {"request": request, "emp": employees})

@router.get("/projects", response_class=HTMLResponse)
async def list_projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "projects": project_list})

@router.get("/create-project", response_class=HTMLResponse)
async def create_project_form(request: Request):
    # Pass an empty project object to the template.
    return templates.TemplateResponse("create-project.html", {"request": request, "project": {}})

@router.post("/save-project", response_class=HTMLResponse)
async def save_project_submission(
    request: Request,
    id: int = Form(None),
    title: str = Form(...),
    type: str = Form(...),
    color: str = Form(""),
    description: str = Form(""),
    days: int = Form(0),
    price: float = Form(0.0),
    featured: bool = Form(False),
    launchDate: str = Form(None)
):
    # TODO create a new Project and add it to the projects list
    project = Project()

    return templates.TemplateResponse("result.html", {"request": request, "project": project})

@router.get("/counters", response_class=HTMLResponse)
async def counters(request: Request):
    # Manual session counter stored under key "counter"
    session = request.session
    counter_manual = session.get("counter", 0) + 1
    session["counter"] = counter_manual

    # Request-scoped counter: a new Counter instance per request.
    request_counter = Counter().next()

    # Session-scoped counter simulation: stored under key "nSession2"
    session_counter2 = session.get("nSession2", 0) + 1
    session["nSession2"] = session_counter2

    # Application-scoped counter: stored globally in app state.
    application_counter: Counter = request.app.state.application_counter
    application_counter_value = application_counter.next()

    return templates.TemplateResponse("counter.html", {
        "request": request,
        "sessioncounter": counter_manual,
        "requestcounter2": request_counter,
        "sessioncounter2": session_counter2,
        "applicationcounter2": application_counter_value
    })

# Simulated servlet: returns a simple "Hello World!" HTML snippet.
@router.get("/exampleServlet/AnnotationExample", response_class=HTMLResponse)
async def example_servlet(request: Request):
    html_content = "<p>Hello World!</p>"
    return HTMLResponse(content=html_content)

# Simulated ThymeleafServlet endpoints using Jinja2.
@router.get("/thymeleafServlet/hellofromservlet.html", response_class=HTMLResponse)
async def thymeleaf_hellofromservlet(request: Request):
    return servlet_templates.TemplateResponse("hellofromservlet.html", {
        "request": request,
        "name": "friendly student!!!!!",
        "thename": "Jonas",
        "completeurl": "http://localhost:8080/thymeleafServlet/hellofromservlet.html"
    })

@router.get("/thymeleafServlet/urls.html", response_class=HTMLResponse)
async def thymeleaf_urls(request: Request):
    return servlet_templates.TemplateResponse("urls.html", {
        "request": request,
        "name": "friendly student!!!!!",
        "thename": "Jonas",
        "completeurl": "http://localhost:8080/thymeleafServlet/urls.html"
    })
