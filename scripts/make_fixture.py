#!/usr/bin/env python3
"""Build a throwaway repository for eval runs that have tools enabled.

Cases that name a file need that file to exist, otherwise a tool-enabled run
spends its turn searching and never answers. Rebuild before every run so each
run starts from identical state.

    python3 scripts/make_fixture.py /tmp/bro-fixture
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

FILES: dict[str, str] = {
    "README.md": (
        "# Ledger\n\n"
        "A small tool for tracking supplier invoices.\n\n"
        "Imports run nightly. Any address that fails validation is queued for "
        "review, and the operator will recieve a summary the following morning.\n\n"
        "## Install\n\n```bash\nbun install\n```\n"
    ),
    "src/components/Card.tsx": (
        "import { formatCurrency } from './utils/format'\n\n"
        "export function Card({ amount }: { amount: number }) {\n"
        "  return <div className=\"card\">{formatCurrency(amount)}</div>\n"
        "}\n"
    ),
    "src/lib/format.ts": (
        "export function formatCurrency(value: number): string {\n"
        "  return new Intl.NumberFormat('en-AU', { style: 'currency', currency: 'AUD' }).format(value)\n"
        "}\n"
    ),
    "src/auth.ts": (
        "// 1\n" * 41
        + "export async function sendMagicLink(email: string) {\n"
        "  const token = crypto.randomUUID()\n"
        "  await store.set(`magic:${token}`, email, { ttl: 900 })\n"
        "  return mailer.send(email, `/login?token=${token}`)\n"
        "}\n"
    ),
    "src/Sidebar.tsx": (
        "import { useState, useEffect, useRef } from 'react'\n\n"
        "export function Sidebar() {\n"
        "  const [collapsed, setCollapsed] = useState(false)\n"
        "  const [heights, setHeights] = useState<number[]>([])\n"
        "  const ref = useRef<HTMLUListElement>(null)\n\n"
        "  useEffect(() => {\n"
        "    if (!ref.current) return\n"
        "    setHeights([...ref.current.children].map((el) => el.getBoundingClientRect().height))\n"
        "  }, [collapsed])\n\n"
        "  return (\n"
        "    <nav style={{ transition: 'width 200ms' }}>\n"
        "      <button onClick={() => setCollapsed((c) => !c)}>Toggle</button>\n"
        "      <ul ref={ref}>{/* nav items */}</ul>\n"
        "    </nav>\n"
        "  )\n"
        "}\n"
    ),
    "app/forms/address.rb": (
        "# 1\n" * 33
        + "class AddressForm\n"
        "  include ActiveModel::Model\n"
        "  validates :postcode, format: { with: /\\A\\d{4}\\z/ }\n"
        "end\n"
    ),
}


def build(target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    for relative, body in FILES.items():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    notes = target / "notes"
    notes.mkdir(parents=True, exist_ok=True)
    topics = ["pricing", "hiring", "infra", "writing", "design", "process"]
    for index in range(200):
        topic = topics[index % len(topics)]
        (notes / f"note-{index:03d}.md").write_text(
            f"# Note {index}\n\nA short thought about {topic}.\n", encoding="utf-8"
        )


if __name__ == "__main__":
    destination = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/bro-fixture")
    build(destination)
    print(f"fixture built at {destination}")
