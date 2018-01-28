class Team(object):

    def __init__(self, client):
        self.client = client

    def list_for_org(self, org_username):
        # GET /orgs/{org_username}/teams
        response = self.client.orgs(org_username).teams.GET()
        return response.json()

    def list_for_project(self, project_id):
        # GET /projects/{project_id}/teams
        response = self.client.projects(project_id).teams.GET()
        return response.json()

    def list_for_secret(self, secret_id):
        # GET /secrets/{secret_id}/teams
        response = self.client.secrets(secret_id).teams.GET()
        return response.json()

    def create_for_org(self, org_id, params=None):
        # POST /orgs/{org_username}/teams
        # TODO: Pass params to POST request
        response = self.client.orgs(org_id).POST()
        return response.json()

    def get(self, team_id):
        # GET /teams/{id}
        response = self.client.teams(team_id).GET()
        return response.json()

    def update(self, team_id, params=None):
        # PATCH /teams/{id}
        # TODO: Pass params to PATCH
        response = self.client.teams(team_id).PATCH(params)
        return response.json()

    def delete(self, team_id):
        # DELETE /teams/{id}
        # TODO: Figure out correct response
        response = self.client.teams(team_id).DELETE()
        return response.json()
