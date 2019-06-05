import xml.etree.ElementTree as ET



def recursive_build_string(root, string):
    for child in root:
        # if child.tag == "tree":
        #     tree_name = child.attrib.get("id", "None")
        #     print(child.attrib)
        #     string = f"\Tree[.{{{tree_name}}}"
        #     return recursive_build_string(child, string) + " ]\n"
        if child.tag == "node" or child.tag == "leaf":
            # print(child.attrib)
            category = child.attrib.get("cat", "")
            node_type = child.attrib.get("type", "")
            if node_type == "substitution":
                node_type = "$\downarrow$"

            semantic_label = child.attrib.get("sem", "")
            index = child.attrib.get("index", "")
            string += f"\n[.{{{{{category}}}_{{{index}}}^{{{semantic_label}}} {node_type}}} "
            if child.tag == "node":
                string = recursive_build_string(child, string) + "\n]"
            else:
                string += " ]"
        else:
            break
        string += ""
    return string

    # for child in root:
    #     print(child.tag, child.attrib)


if __name__ == "__main__":

    sample_xml_tree = """<?xml version="1.0"?>
<crisp-grammar>
    <tree id="i.nx0Vnx1Pnx2">
        <node cat="S" index="r" sem="self">
            <leaf cat="NP" type="substitution" index="0" sem="subj"/>
            <node cat="VP" sem="self">
                <leaf cat="V" type="anchor" sem="self"/>
                <leaf cat="NP" type="substitution" index="1" sem="obj"/>
                <node cat="VP" index="e" sem="self">
                    <node cat="V" index="e" sem="self">
                    <leaf cat="" type="terminal" index="v" sem="self"/>
                    </node>
                    <node cat="PP" sem="ppobj">
                        <leaf cat="P" type="lex" sem="ppobj"/>
                        <leaf cat="NP" type="substitution" index="2" sem="ppobj"/>
                    </node>
                </node>
            </node>
        </node>
    </tree> 
      <tree id="i.Dn">   <!-- non-XTAG -->
    <node cat="NP" index="r" sem="self">
      <leaf cat="D" type="anchor" sem="self" />
      <node type="substitution" cat="N" index="0" sem="self" />
    </node>
  </tree>




  <!-- ~~~~~~~ -->
  <!-- LEXICON -->
  <!-- ~~~~~~~ -->

  <entry word='' pos=''>
    <tree refid="tt">
      <semcontent></semcontent>
      <semreq></semreq>
    </tree>
  </entry>

  <entry word='at' pos=''>
    <tree refid="asdfg">
      <semcontent></semcontent>
      <semreq></semreq>
    </tree>
  </entry>
</crisp-grammar>"""

    other_sample = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

    root = ET.fromstring(other_sample)
    root = ET.fromstring(sample_xml_tree)

    # root = ET.parse("../../crisp-nlg/branches/mscrisp/grammars/test_fiction/zombie_domain.pddl")
    root = ET.parse("grammar-zombie.xml")

    print(root.getroot())

    for child in root.getroot():
        if child.tag == "tree":
            print(recursive_build_string(child, f"\Tree[.{{{child.attrib.get('id')}}} ") + " \n]\n\\\\ \\ \\\\")
