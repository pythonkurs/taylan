import untangle
 
def repair_fraction():
    xml_file = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    doc = untangle.parse(xml_file)
    outages = doc.NYCOutages.outage

    outages_count = len(outages)
    repair_count = 0

    for outage in outages:
        if outage.reason.cdata == "REPAIR":
            repair_count += 1
    
    fractionRepair = repair_count / float(outages_count)
    return fractionRepair
