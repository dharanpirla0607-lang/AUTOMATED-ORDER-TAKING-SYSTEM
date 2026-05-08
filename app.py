# ============================================================
# MODULE 1: ARRAY  (Menu Storage)
# ------------------------------------------------------------
# The entire food menu is stored in a Python list (array).
# Each element is a dictionary representing one menu item.
# Array allows O(1) indexed access and O(n) linear search.
# Functions provided:
#   get_menu()         → return the full menu array
#   get_item_by_id(id) → linear search to find one item
# ============================================================

MENU = [
    # ── South Indian Breakfast ────────────────────────────────
    {
        "id": 1,
        "name": "Dosa",
        "emoji": "🥞",
        "price": 60,
        "description": "Crispy South Indian crepe made from fermented rice batter.",
        "grad": "linear-gradient(135deg,#f6d365,#fda085)"
    },
    {
        "id": 2,
        "name": "Idli",
        "emoji": "⬜",
        "price": 40,
        "description": "Soft steamed rice cakes served with sambar and chutney.",
        "grad": "linear-gradient(135deg,#e0eafc,#cfdef3)"
    },
    {
        "id": 3,
        "name": "Vada",
        "emoji": "🍩",
        "price": 30,
        "description": "Crispy fried lentil doughnuts, perfect with coconut chutney.",
        "grad": "linear-gradient(135deg,#c471f5,#fa71cd)"
    },
    # ── Breads ───────────────────────────────────────────────
    {
        "id": 4,
        "name": "Roti",
        "emoji": "🫓",
        "price": 15,
        "description": "Soft whole wheat flatbread, a wholesome North Indian staple.",
        "grad": "linear-gradient(135deg,#ffecd2,#fcb69f)"
    },
    {
        "id": 5,
        "name": "Parotta",
        "emoji": "🥙",
        "price": 20,
        "description": "Flaky layered flatbread from South India, served with curry.",
        "grad": "linear-gradient(135deg,#d4fc79,#96e6a1)"
    },
    # ── Rice Dishes ──────────────────────────────────────────
    {
        "id": 6,
        "name": "Paneer Biryani",
        "emoji": "🍛",
        "price": 120,
        "description": "Aromatic basmati rice slow-cooked with spiced paneer and whole spices.",
        "grad": "linear-gradient(135deg,#f093fb,#f5576c)"
    },
    {
        "id": 7,
        "name": "Veg Fried Rice",
        "emoji": "🍳",
        "price": 80,
        "description": "Stir-fried basmati rice tossed with colourful vegetables and soy sauce.",
        "grad": "linear-gradient(135deg,#4facfe,#00f2fe)"
    },
    # ── Curries ──────────────────────────────────────────────
    {
        "id": 8,
        "name": "Paneer Butter Masala",
        "emoji": "🧆",
        "price": 130,
        "description": "Rich creamy tomato-based curry loaded with golden paneer cubes.",
        "grad": "linear-gradient(135deg,#fa709a,#fee140)"
    },
    {
        "id": 9,
        "name": "Chole Curry",
        "emoji": "🫘",
        "price": 90,
        "description": "Spicy chickpea curry simmered in tangy onion-tomato gravy.",
        "grad": "linear-gradient(135deg,#30cfd0,#330867)"
    },
    {
        "id": 10,
        "name": "Dum Aloo",
        "emoji": "🥔",
        "price": 100,
        "description": "Baby potatoes slow-cooked in an aromatic spiced yogurt gravy.",
        "grad": "linear-gradient(135deg,#a1c4fd,#c2e9fb)"
    },
    {
        "id": 11,
        "name": "Jeera Aloo",
        "emoji": "🥔",
        "price": 70,
        "description": "Potatoes tempered with cumin seeds, fresh coriander, and spices.",
        "grad": "linear-gradient(135deg,#fddb92,#d1fdff)"
    },
    # ── Starters ─────────────────────────────────────────────
    {
        "id": 12,
        "name": "Paneer Tikka",
        "emoji": "🍢",
        "price": 150,
        "description": "Smoky grilled paneer marinated in a spiced yogurt and herb mix.",
        "grad": "linear-gradient(135deg,#f77062,#fe5196)"
    },
    {
        "id": 13,
        "name": "Veg Manchurian",
        "emoji": "🥡",
        "price": 80,
        "description": "Crispy vegetable balls tossed in a tangy Indo-Chinese sauce.",
        "grad": "linear-gradient(135deg,#e0c3fc,#8ec5fc)"
    },
    # ── Comfort Food ─────────────────────────────────────────
    {
        "id": 14,
        "name": "Curd Rice",
        "emoji": "🍚",
        "price": 50,
        "description": "Comforting South Indian curd rice tempered with mustard and curry leaves.",
        "grad": "linear-gradient(135deg,#f5f7fa,#b8c6db)"
    },
    # ── Beverages ────────────────────────────────────────────
    {
        "id": 15,
        "name": "Rose Milk",
        "emoji": "🌹",
        "price": 30,
        "description": "Refreshing chilled milk flavoured with fragrant rose syrup.",
        "grad": "linear-gradient(135deg,#fbc2eb,#a6c1ee)"
    },
    {
        "id": 16,
        "name": "Pista Milk",
        "emoji": "🍃",
        "price": 40,
        "description": "Creamy chilled milk enriched with pistachio flavour and nuts.",
        "grad": "linear-gradient(135deg,#84fab0,#8fd3f4)"
    },
    {
        "id": 17,
        "name": "Badam Milk",
        "emoji": "🥛",
        "price": 40,
        "description": "Warm or chilled milk infused with almond paste and a hint of saffron.",
        "grad": "linear-gradient(135deg,#ffeaa7,#fdcb6e)"
    },
    # ── Desserts ─────────────────────────────────────────────
    {
        "id": 18,
        "name": "Chocolate Ice Cream",
        "emoji": "🍫",
        "price": 60,
        "description": "Rich and creamy ice cream made from premium dark chocolate.",
        "grad": "linear-gradient(135deg,#6d3b2d,#a0522d)"
    },
    {
        "id": 19,
        "name": "Vanilla Ice Cream",
        "emoji": "🍦",
        "price": 50,
        "description": "Classic smooth and velvety ice cream with pure vanilla bean flavour.",
        "grad": "linear-gradient(135deg,#fffde7,#ffe0b2)"
    },
    {
        "id": 20,
        "name": "Butterscotch Ice Cream",
        "emoji": "🍨",
        "price": 60,
        "description": "Sweet buttery ice cream swirled with rich caramel butterscotch.",
        "grad": "linear-gradient(135deg,#f6d365,#fda085)"
    },
]


# ── Stock tracking (MODULE 1: ARRAY / Set) ───────────────
# A Python set stores IDs of out-of-stock items.
# Set gives O(1) lookup for stock checks.
OUT_OF_STOCK: set = set()


def get_menu():
    """Return the complete menu array."""
    return MENU


def get_menu_with_stock():
    """Return menu array with live in_stock flag on each item."""
    result = []
    for item in MENU:
        entry = dict(item)                          # shallow copy
        entry['in_stock'] = item['id'] not in OUT_OF_STOCK
        result.append(entry)
    return result


def get_item_by_id(item_id):
    """
    Linear search through the MENU array to find item by ID.
    Time complexity: O(n)
    """
    for item in MENU:
        if item["id"] == item_id:
            return item
    return None


def is_out_of_stock(item_id: int) -> bool:
    """O(1) set lookup to check if an item is out of stock."""
    return item_id in OUT_OF_STOCK


def toggle_stock(item_id: int) -> bool:
    """
    Toggle the stock status of an item.
    Returns True  if item is NOW out of stock.
    Returns False if item is NOW back in stock.
    """
    if item_id in OUT_OF_STOCK:
        OUT_OF_STOCK.discard(item_id)   # mark as in stock
        return False
    else:
        OUT_OF_STOCK.add(item_id)       # mark as out of stock
        return True


def set_out_of_stock(item_id: int):
    """Explicitly mark an item as out of stock."""
    OUT_OF_STOCK.add(item_id)


def set_in_stock(item_id: int):
    """Explicitly mark an item as in stock."""
    OUT_OF_STOCK.discard(item_id)
