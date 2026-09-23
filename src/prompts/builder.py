from src.prompts.core import AEGIS_CORE
from src.prompts.normal import NORMAL_PROFILE
from src.prompts.red.core import RED_CORE
from src.prompts.red.pentest import PENTEST_MODULE


RED_MODULES = {
	"pentest": PENTEST_MODULE,
}

def build_normal_prompt():
	return f"{AEGIS_CORE.strip()}\n\n{NORMAL_PROFILE.strip()}"


def build_red_prompt(module=None):
    parts = [
        AEGIS_CORE.strip(),
        RED_CORE.strip(),
    ]

    if module is not None:
        if module not in RED_MODULES:
            raise ValueError(f"Modulo RED non valido: {module}")

        parts.append(RED_MODULES[module].strip())

    return "\n\n".join(parts)
