"""
FunAPI App
"""

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.utils.load_json import load_json
from app.utils.get_random import get_random

from app.models.compliment import Compliment
from app.models.fortune import Fortune
from app.models.fun_fact import FunFact
from app.models.life_truth import LifeTruth
from app.models.pizza_idea import PizzaIdea
from app.models.thought import Thought

app = FastAPI(
    title="FunAPI",
    # pylint: disable=C0301
    description="FunAPI provides random compliments, fortunes, pizza ideas, life truths, and thoughts.",
    version="1.0",
    contact={"name": "Lakhindar Pal", "url": "https://lakhindar.is-a-good.dev"},
    license_info={
        "name": "MIT",
        "url": "https://github.com/LakhindarPal/my-fun-api/blob/main/LICENSE",
        "identifier": "MIT",
    },
)


compliments = load_json("compliments.json")
fortunes = load_json("fortunes.json")
funfacts = load_json("funfacts.json")
lifetruths = load_json("lifetruths.json")
pizzaideas = load_json("pizzaideas.json")
thoughts = load_json("thoughts.json")


@app.get("/", include_in_schema=False)
async def scalar_html():
    """
    Get the Scalar documentation of the API.

    Returns: str
    """
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title + " - Scalar",
    )


@app.get("/compliment")
async def random_compliment() -> Compliment:
    """
    Brighten up your day with a random compliment.

    Returns: Compliment
    """
    return Compliment(
        success=True,
        data={"compliment": get_random(compliments)},
    )


@app.get("/fortune")
async def random_fortune() -> Fortune:
    """
    Ponder upon random fortunes for insight and inspiration.

    Returns: Fortune
    """
    return Fortune(
        success=True,
        data={"fortune": get_random(fortunes)},
    )


@app.get("/funfact")
async def random_fun_fact() -> FunFact:
    """
    Discover random useless yet interesting fact.

    Returns: FunFact
    """
    return FunFact(
        success=True,
        data={"fun_fact": get_random(funfacts)},
    )


@app.get("/lifetruth")
async def random_life_truth() -> LifeTruth:
    """
    Reflect on deep life truths that resonate with you.

    Returns: LifeTruth
    """
    return LifeTruth(
        success=True,
        data={"life_truth": get_random(lifetruths)},
    )


@app.get("/pizzaidea")
async def random_pizza_idea() -> PizzaIdea:
    """
    Get a crazy way to phone in a pizza order.

    Returns: PizzaIdea
    """
    return PizzaIdea(
        success=True,
        data={"pizza_idea": get_random(pizzaideas)},
    )


@app.get("/thought")
async def random_thought() -> Thought:
    """
    Get a random thing to think about.

    Returns: Thought
    """
    return Thought(
        success=True,
        data={"thought": get_random(thoughts)},
    )
