import os
import xml.etree.ElementTree as ET
import streamlit as st
import base64
from io import BytesIO

# ---------- Utility Functions ----------
def hex_to_text(value):
    try:
        if all(c in "0123456789ABCDEFabcdef" for c in value) and len(value) % 2 == 0 and value != "":
            return bytes.fromhex(value).decode("utf-8")
    except:
        pass
    return value

def text_to_hex(value):
    try:
        return value.encode("utf-8").hex()
    except:
        return value


# ---------- XML Parsing ----------
def parse_xml(uploaded_file):
    try:
        tree = ET.parse(uploaded_file)
        root = tree.getroot()
        return tree, root
    except Exception as e:
        st.error(f"Error loading XML: {e}")
        return None, None


# ---------- Recursive Tree Display ----------
def display_node(node, level=0):
    name = node.attrib.get("NAME", "")
    type_ = node.attrib.get("TYPE", "")
    value = hex_to_text(node.attrib.get("VALUE", ""))

    # UI for a node
    col1, col2, col3 = st.columns([3, 2, 3])
    with col1:
        st.text_input(f"Name (Level {level})", value=name, key=f"name_{id(node)}_{level}", disabled=True)
    with col2:
        st.text_input("Type", value=type_, key=f"type_{id(node)}_{level}", disabled=True)
    with col3:
        new_val = st.text_input("Value", value=value, key=f"value_{id(node)}_{level}")

        # Save the edited value back into XML
        if new_val != value:
            node.set("VALUE", text_to_hex(new_val) if not all(c in "0123456789ABCDEFabcdef" for c in new_val) else new_val)

    # Display child nodes recursively
    for child in node:
        with st.expander(f"Child Node: {child.attrib.get('NAME', '')}", expanded=False):
            display_node(child, level + 1)


# ---------- Comparison ----------
def compare_nodes(node1, node2, differences, path=""):
    if (
        node1.attrib.get("NAME") != node2.attrib.get("NAME")
        or node1.attrib.get("TYPE") != node2.attrib.get("TYPE")
        or node1.attrib.get("VALUE") != node2.attrib.get("VALUE")
    ):
        differences.append(path or node1.attrib.get("NAME", "ROOT"))

    for i, (c1, c2) in enumerate(zip(list(node1), list(node2))):
        compare_nodes(c1, c2, differences, f"{path}/{c1.attrib.get('NAME', '')}")


def compare_xmls(root1, root2):
    differences = []
    nodes1 = root1.findall("NODE")
    nodes2 = root2.findall("NODE")

    for i, (n1, n2) in enumerate(zip(nodes1, nodes2)):
        compare_nodes(n1, n2, differences, n1.attrib.get("NAME", f"Node{i}"))

    return differences


# ---------- XML Download ----------
def xml_to_download_link(tree, filename):
    xml_bytes = ET.tostring(tree.getroot(), encoding="utf-8", method="xml")
    b64 = base64.b64encode(xml_bytes).decode()
    href = f'<a href="data:file/xml;base64,{b64}" download="{filename}">📥 Download {filename}</a>'
    return href


# ---------- Streamlit App ----------
st.set_page_config(page_title="XML Compare Editor", layout="wide")
st.title("🧩 XML Compare Editor (Streamlit Version)")

# Maintain session state for XMLs
if "tree1" not in st.session_state:
    st.session_state.tree1, st.session_state.root1 = None, None
if "tree2" not in st.session_state:
    st.session_state.tree2, st.session_state.root2 = None, None

col1, col2 = st.columns(2)

with col1:
    st.header("XML 1")
    xml_file1 = st.file_uploader("Upload XML File 1", type=["xml"], key="xml1")
    if xml_file1:
        st.session_state.tree1, st.session_state.root1 = parse_xml(xml_file1)
    if st.session_state.root1:
        with st.expander("View/Edit XML 1", expanded=True):
            for node in st.session_state.root1.findall("NODE"):
                display_node(node)

with col2:
    st.header("XML 2")
    xml_file2 = st.file_uploader("Upload XML File 2", type=["xml"], key="xml2")
    if xml_file2:
        st.session_state.tree2, st.session_state.root2 = parse_xml(xml_file2)
    if st.session_state.root2:
        with st.expander("View/Edit XML 2", expanded=True):
            for node in st.session_state.root2.findall("NODE"):
                display_node(node)

st.divider()

# ---------- Compare Button ----------
if st.button("🔍 Compare XMLs"):
    if st.session_state.root1 is None or st.session_state.root2 is None:
        st.warning("Please upload both XML files.")
    else:
        diffs = compare_xmls(st.session_state.root1, st.session_state.root2)
        if diffs:
            st.error(f"Differences found in {len(diffs)} nodes:")
            for d in diffs:
                st.write(f" - {d}")
        else:
            st.success("✅ No differences found. XMLs are identical.")

st.divider()

# ---------- Save / Download ----------
if st.session_state.tree1:
    st.markdown(xml_to_download_link(st.session_state.tree1, "XML1_updated.xml"), unsafe_allow_html=True)
if st.session_state.tree2:
    st.markdown(xml_to_download_link(st.session_state.tree2, "XML2_updated.xml"), unsafe_allow_html=True)
