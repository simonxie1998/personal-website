SUMMARIES = {
    "ontology_p1": "For context, AKASA automates revenue cycle operation workflows with RPA and ML. Ontology is a state tracker of the bots within an EHR (Electronic Health Record), "
    "so it keeps track of where the bot is within the application as well as how it got there. Ontology also stores the navigation network graph of the configured edges and nodes "
    "allowing it to be able to find a path to certain parts of the EHR regardless of the starting point. This graph had previously been configured with yamls in the repository, so any "
    "updates to the graph will require manual configuration of the engineer. This poses 3 problems: manual configuration is error prone, it requires engineering bandwidth, there's no "
    "standardization of the yaml names/location in the repository polluting it.",
    "ontology_p2": "In a 2 day hacakthon project in March 2022, I built a full fledged CRUD application that allows any user to build an ontology graph. This allows product managers or "
    "operations team members to free up time for engineers, validates inputs within the application, and abstracts the yamls into an endpoint allowing engineers "
    "to not even have to look at a yaml anymore. This application also supported much more funcationality than just building the graph. It supported versioning logic "
    "to undo/redo operations and permanent versioning so that production configurations can be used. Other functionality included toggling on/off labels in the graph, "
    "importing existing yamls, downloading the graph as a yaml, and downloading a change log.",
}
