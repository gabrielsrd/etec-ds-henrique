"""Conversão Markdown -> HTML usada pela plataforma (pandoc gfm + callouts estilo GitHub)."""
import re
import subprocess

CALLOUT_RE = re.compile(r'^>\s*\[!(WARNING|CAUTION|NOTE|TIP|IMPORTANT)\]\s*(.*)$')


def convert_alerts(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = CALLOUT_RE.match(lines[i])
        if m:
            kind = m.group(1).lower()
            block = [m.group(2)] if m.group(2).strip() else []
            i += 1
            while i < len(lines) and lines[i].startswith('>'):
                block.append(re.sub(r'^>\s?', '', lines[i]))
                i += 1
            out.append(f'<div class="callout callout-{kind}">\n\n' + "\n".join(block) + "\n\n</div>\n")
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def md_to_html(md_text: str) -> str:
    html = subprocess.check_output(
        ["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
        input=convert_alerts(md_text),
        text=True,
    )
    html = html.replace("<table>", '<div class="table-wrap"><table class="q-table">')
    html = html.replace("</table>", "</table></div>")
    return html


def md_inline(text: str) -> str:
    """Converte um trecho curto (enunciado, alternativa, explicação) sem envolver em <p>."""
    html = md_to_html(text).strip()
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        html = html[3:-4]
    return html
