# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.frontpage -t test_section.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.frontpage.testing.COLLECTIVE_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/frontpage/tests/robot/test_section.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Section
  Given a logged-in site administrator
    and an add Frontpage form
   When I type 'My Section' into the title field
    and I submit the form
   Then a Section with the title 'My Section' has been created

Scenario: As a site administrator I can view a Section
  Given a logged-in site administrator
    and a Section 'My Section'
   When I go to the Section view
   Then I can see the Section title 'My Section'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Frontpage form
  Go To  ${PLONE_URL}/++add++Frontpage

a Section 'My Section'
  Create content  type=Frontpage  id=my-section  title=My Section

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Section view
  Go To  ${PLONE_URL}/my-section
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Section with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Section title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
