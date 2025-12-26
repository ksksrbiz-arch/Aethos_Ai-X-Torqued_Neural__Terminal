from aethos_ai.core.identity import AethosProfile
from aethos_ai.core.story import generate_origin_story


def test_generate_origin_story_includes_name_and_values():
    profile = AethosProfile(name="Aethos", values=["Curiosity", "Empathy"])
    story = generate_origin_story(profile, include_timestamp=False)

    assert "Aethos" in story
    assert "Curiosity" in story
    assert "Empathy" in story
