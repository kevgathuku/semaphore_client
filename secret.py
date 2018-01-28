class Secret(object):

    def __init__(self, client):
        self.client = client

    def list_for_org(self, org):
        # GET /orgs/{org_username}/secrets
        response = self.client.orgs(org_username).secrets.GET()
        return response.json()

    def list_for_team(self, team_id):
        # GET /teams/{team_id}/secrets
        response = self.client.teams(team_id).secrets.GET()
        return response.json()

    def list_for_project(self, project_id):
        # GET /projects/{project_id}/secrets
        response = self.client.projects(project_id).secrets.GET()
        return response.json()

    def create_in_org(self, org_username, params=None):
        # POST /orgs/{org_username}/secrets
        # TODO: Pass params to POST request
        response = self.client.orgs(org_username).secrets.POST()
        return response.json()

    def get(self, secret_id):
        # GET /secrets/{id}
        response = self.client.secrets(secret_id).GET()
        return response.json()

    def update(self, secret_id):
        # PATCH /secrets/{id}
         # TODO: Pass params to PATCH
        response = self.client.secrets(secret_id).PATCH(params)
        return response.json()

    def delete(self):
        # DELETE /secrets/{id}
        # TODO: Figure out correct response
        response = self.client.secrets(secret_id).DELETE()
        return response.json()

    def attach_to_team(self, secret=secret_id, team=team_id):
        # POST /teams/{team_id}/secrets/{secret_id}
        response = self.client.teams(team).secrets(secret).POST()
        return response.json()

    def attach_to_project(self, secret=secret_id, project=project_id):
        # POST /projects/{project_id}/secrets/{secret_id}
        response = self.client.projects(project).secrets(secret).POST()
        return response.json()

    def detach_from_team(self, secret=secret_id, team=team_id):
        # DELETE /teams/{team_id}/secrets/{secret_id}
        response = self.client.teams(team).secrets(secret).DELETE()
        return response.json()

    def detach_from_project(self, secret=secret_id, project=project_id):
        # DELETE /projects/{project_id}/secrets/{secret_id}
        response = self.client.projects(project).secrets(secret).DELETE()
        return response.json()
