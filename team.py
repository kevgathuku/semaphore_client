class Team(object):

    def __init__(self, client):
        self.client = client

    def list_for_org(self, org_id):
        # path = f"/orgs/{org_id}/teams"
        response = self.client.orgs(org_id).teams.GET()
        return response.json()

    def list_for_project(self, project_id):
        # /projects/{project_id}/teams
        response = self.client.projects(project_id).teams.GET()
        return response.json()

    def list_for_secret(self, secret_id):
        # /secrets/{secret_id}/teams
        response = self.client.secrets(secret_id).teams.GET()
        return response.json()

    def create_for_org(self, org_id):
        pass

    def get(self, team_id):
        # /teams/{id}
        response = self.client.teams(team_id).GET()
        return response.json()

    def update(self, team_id):
        pass

    def delete(self, team_id):
        pass
